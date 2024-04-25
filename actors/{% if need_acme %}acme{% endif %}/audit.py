# Demo file to show example of audit actors. Feel free to adjust or remove
from zodchy import codex
from zodchy_patterns import events

import specs


def create(
    frame: codex.Frame[specs.messages.CreateSomething, specs.context.CreateSomethingAuditContext],
    auth_context: specs.context.RequestAuthContext
) -> specs.messages.CreateSomething | events.HttpAuthError:
    if frame.context.owner_id != auth_context.user_id:
        return events.HttpAuthError()
    return frame.payload
