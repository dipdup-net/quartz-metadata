from dipdup.context import HookContext


async def resolver_job(
    ctx: HookContext,
) -> None:
    await ctx.callbacks.run()
