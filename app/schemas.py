from pydantic import BaseModel


class PlanBase(BaseModel):
    name: str
    description: str
    permissions: str
    usage_limit: int


class PermissionBase(BaseModel):
    name: str
    description: str


class SubscriptionBase(BaseModel):
    user_id: int
    plan_id: int


class UserBase(BaseModel):
    username: str
    status: str


class UsageBase(BaseModel):
    user_id: int


class PlanCreate(PlanBase):
    pass


class PermissionCreate(PermissionBase):
    pass


class SubscriptionCreate(SubscriptionBase):
    pass


class UserCreate(UserBase):
    pass


class UsageCreate(UsageBase):
    pass
