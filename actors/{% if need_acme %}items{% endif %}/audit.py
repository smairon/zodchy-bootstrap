# Demo file to show example of audit actors. Feel free to adjust or remove
from zodchy import codex
from zodchy_patterns import events

import specs


def create(
    frame: codex.cqea.Frame[specs.messages.CreateItem, specs.context.CreateItemAuditContext],
    auth_context: specs.context.RequestAuthContext
) -> specs.messages.CreateItem | events.HttpAuthError:
    if frame.context.user_id != auth_context.user_id:
        return events.HttpAuthError()
    return frame.payload
