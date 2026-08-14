from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from app.schemas import TaskCreate, TaskUpdate, TaskBase
from database import services

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskBase, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await services.add_task(
        session=session,
        title=task_in.title,
        description=task_in.description,
        is_completed=task_in.is_completed,
    )


@router.patch("/{task_id}", response_model=TaskBase, status_code=status.HTTP_200_OK)
async def patch_task(
    task_id: int,
    task_in: TaskUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    updated_task = await services.update_task(
        session=session,
        task_id=task_id,
        title=task_in.title,
        description=task_in.description,
        is_completed=task_in.is_completed,
    )
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_task(
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    deleted = await services.delete_task(session=session, task_id=task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return None