from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Task


async def add_task(
    session: AsyncSession,
    title: str,
    description: str | None = None,
    is_completed: bool = False,
) -> Task:
    new_task = Task(title=title, description=description, is_completed=is_completed)
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


async def update_task(
    session: AsyncSession,
    task_id: int,
    title: str,
    description: str | None = None,
    is_completed: bool | None = None,
) -> Task | None:
    query = select(Task).where(Task.id == task_id)
    result = await session.execute(query)
    task = result.scalar_one_or_none()

    if not task:
        return None
    
    if title is not None: 
        task.title = title 

    if description is not None:
        task.description = description
    if is_completed is not None:
        task.is_completed = is_completed

    await session.commit()
    await session.refresh(task)
    return task


async def delete_task(
    session: AsyncSession,
    task_id: int,
) -> bool:
    query = select(Task).where(Task.id == task_id)
    result = await session.execute(query)
    task = result.scalar_one_or_none()

    if not task:
        return False

    await session.delete(task)
    await session.commit()
    return True