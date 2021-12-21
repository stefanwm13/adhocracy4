import rules

from adhocracy4.modules import predicates as module_predicates

from . import models

rules.add_perm(
    'a4polls.change_poll',
    module_predicates.is_allowed_crud_project
)

rules.add_perm(
    'a4polls.view_poll',
    (module_predicates.is_allowed_moderate_project |
     module_predicates.is_allowed_view_item)
)

rules.add_perm(
    'a4polls.comment_poll',
    module_predicates.is_allowed_comment_item
)


# It has to be ensured that the permission is always checked against a module
# never a Vote object.
rules.add_perm(
    'a4polls.add_vote',
    module_predicates.is_allowed_add_item(models.Vote)
)
