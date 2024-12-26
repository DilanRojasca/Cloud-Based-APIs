from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import services
from .schemas import PlanCreate, PermissionCreate, UserCreate, SubscriptionCreate
from .database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/plans/", response_model=PlanCreate)
async def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    return services.create_plan(db=db, plan=plan)


@router.get("/plans/{plan_id}", response_model=PlanCreate)
async def get_plan(plan_id: int, db: Session = Depends(get_db)):
    db_plan = services.get_plan(db=db, plan_id=plan_id)
    if db_plan:
        return db_plan
    raise HTTPException(status_code=404, detail="Plan not found")


@router.put("/plans/{plan_id}", response_model=PlanCreate)
async def update_plan(plan_id: int, plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = services.update_plan(db=db, plan_id=plan_id, plan=plan)
    if db_plan:
        return db_plan
    raise HTTPException(status_code=404, detail="Plan not found")


@router.delete("/plans/{plan_id}", response_model=PlanCreate)
async def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    db_plan = services.delete_plan(db=db, plan_id=plan_id)
    if db_plan:
        return db_plan
    raise HTTPException(status_code=404, detail="Plan not found")


@router.post("/permissions/", response_model=PermissionCreate)
async def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    return services.create_permission(db=db, permission=permission)


@router.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db=db, user=user)


@router.post("/subscriptions/", response_model=SubscriptionCreate)
async def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    return services.create_subscription(db=db, subscription=subscription)
