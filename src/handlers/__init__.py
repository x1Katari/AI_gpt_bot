from aiogram import Router


def setup_routers() -> Router:
  from .user import start, menu, dialog
  from .admin import sample

  router = Router()
  router.include_routers(
    start.start_router,
    menu.menu_router,
    sample.sample_router,
    dialog.dialog_router,
  )

  return router
