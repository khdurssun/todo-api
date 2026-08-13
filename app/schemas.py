from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    description: str | None = None
    is_completed: bool = False


class TaskCreate(TaskBase):
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=5, max_length=100)
    is_completed: bool 


class TaskUpdate(BaseModel):
    title: str | None = Field(min_length=1, max_length=50)
    description: str | None = None
    is_completed: bool | None = None


class Task(TaskBase):
    id: int

    model_config = ConfigDict(from_attributes=True)