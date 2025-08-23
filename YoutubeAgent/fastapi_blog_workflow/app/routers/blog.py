from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.request import BlogInput
from app.models.response import BlogResponse
from app.models.state import BlogState
from app.services.workflow import run_blog_workflow
from app.services import workflow_store

router = APIRouter(prefix="/blog", tags=["Blog"])


def _build_response(workflow_id: str, state: BlogState) -> dict:
    """
    Helper to standardize workflow responses.
    """
    if state.get("approved") is None:
        return {
            "workflow_id": workflow_id,
            "status": "paused",
            "pause_reason": "waiting_for_approval",
            "state": state,
        }
    elif state.get("postMedia") is None:
        return {
            "workflow_id": workflow_id,
            "status": "paused",
            "pause_reason": "waiting_for_media_choice",
            "state": state,
        }
    elif state.get("finalpost"):
        return {
            "workflow_id": workflow_id,
            "status": "finished",
            "state": state,
        }
    else:
        return {
            "workflow_id": workflow_id,
            "status": "running",
            "state": state,
        }


@router.post("/start")
async def start_workflow(req: BlogInput, db: Session = Depends(workflow_store.get_db)):
    """
    Start workflow, returns workflow_id and initial state.
    """
    initial_state: BlogState = {
        "input": {"text": req.text, "image_url": req.image_url or ""},
    }  # type: ignore

    # Save workflow
    workflow_id = workflow_store.create_workflow(db, initial_state)

    # Run until first HITL pause
    state = run_blog_workflow(initial_state,workflow_id)
    workflow_store.update_workflow(db, workflow_id, state)
    return _build_response(workflow_id, state) # type: ignore


@router.post("/approve/{workflow_id}")
async def approve_blog(
    workflow_id: str,
    approved: bool,
    feedback: str = "",
    db: Session = Depends(workflow_store.get_db),
):
    """
    API to approve/reject the blog.
    """
    state = workflow_store.get_workflow(db, workflow_id)
    if not state:
        raise HTTPException(404, f"Workflow {workflow_id} not found")

    state["approved"] = approved
    state["feedback"] = feedback

    # Continue workflow
    state = run_blog_workflow(state,workflow_id)  # type: ignore
    workflow_store.update_workflow(db, workflow_id, state)
    return _build_response(workflow_id, state) # type: ignore


@router.post("/choose_media/{workflow_id}")
async def choose_post_media(
    workflow_id: str, post_media: str, db: Session = Depends(workflow_store.get_db)
):
    """
    API to choose post media.
    """
    state = workflow_store.get_workflow(db, workflow_id)
    if not state:
        raise HTTPException(404, f"Workflow {workflow_id} not found")

    if post_media not in ["fb", "instagram"]:
        raise HTTPException(400, "Invalid post_media. Must be 'fb' or 'instagram'")

    state["postMedia"] = post_media

    # Continue workflow
    state = run_blog_workflow(state,workflow_id)  # type: ignore
    workflow_store.update_workflow(db, workflow_id, state)
    return _build_response(workflow_id, state) # type: ignore
