from fastapi import APIRouter

from . import lok
from . import accessory
from . import s88
from . import configs
from . import general
from . import system
from . import camera
from . import switch

router = APIRouter()
router.include_router(
    general.router,
    prefix = "/general",
    tags = ["general"]
)
router.include_router(
    lok.router,
    prefix = "/lok",
    tags = ["lok"]
)
router.include_router(
    accessory.router,
    prefix = "/accessory",
    tags = ["accessory"]
)
router.include_router(
    s88.router,
    prefix = "/s88",
    tags = ["s88"]
)
router.include_router(
    configs.router,
    prefix = "/config",
    tags = ["config"]
)
router.include_router(
    system.router,
    prefix = "/system",
    tags = ["system"]
)

router.include_router(
    camera.router,
    prefix = "/camera",
    tags = ["camera"]
)

router.include_router(
    switch.router,
    prefix = "/switch",
    tags = ["switch"]
)