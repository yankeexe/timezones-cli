import click


class TzAbbrev(click.ParamType):
    name = "Timezone Abbreviation"

    def convert(self, value: str, param: str, ctx) -> str:
        # validate timezone abbreviation length
        if all(c not in value for c in ["+", "-"]) and ctx.params.get("zone"):
            if 2 <= len(value) <= 4:
                return value.upper()
            else:
                click.echo(ctx.command.get_help(ctx))
                raise click.BadParameter(
                    "timezone code needs to be between 2 to 4 letters when using --zone flag"
                )
        return value
