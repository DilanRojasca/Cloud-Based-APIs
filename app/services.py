from sqlalchemy.orm import Session
from .models import Plan, Permission, Subscription, User, Usage
from .schemas import PlanCreate, PermissionCreate, UserCreate, SubscriptionCreate


def create_plan(db: Session, plan: PlanCreate):
    db_plan = Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def get_plan(db: Session, plan_id: int):
    return db.query(Plan).filter(Plan.id == plan_id).first()


def update_plan(db: Session, plan_id: int, plan: PlanCreate):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    for key, value in plan.dict().items():
        setattr(db_plan, key, value)
    db.commit()
    return db_plan


def delete_plan(db: Session, plan_id: int):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    db.delete(db_plan)
    db.commit()
    return db_plan


def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_subscription(db: Session, subscription: SubscriptionCreate):
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription
