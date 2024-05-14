from unionai.remote import UnionRemote
from flytekit.configuration import Config

remote = UnionRemote(config=Config.auto(), default_project=<project-id>, default_domain=<domain>)
launch_plan = remote.fetch_launch_plan(ame=<launch-plan-name>, version=<launch-plan-version>).id
remote.client.update_launch_plan(launch_plan.id, "ACTIVE")
