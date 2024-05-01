import zodchy_fastapi
import zodchy_notations

query_adapter = zodchy_fastapi.adapters.QueryAdapter(
    notation_parser=zodchy_notations.query.math.Parser()
)
