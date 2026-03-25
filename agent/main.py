import sys

from maa.agent.agent_server import AgentServer
from maa.context import Context
from maa.custom_action import CustomAction
from maa.custom_recognition import CustomRecognition
from maa.tasker import Tasker


def main() -> None:
    Tasker.set_log_dir("./debug")

    if len(sys.argv) < 2:
        print("Usage: python agent/main.py <socket_id>")
        raise SystemExit(1)

    socket_id = sys.argv[-1]
    AgentServer.start_up(socket_id)
    AgentServer.join()
    AgentServer.shut_down()


@AgentServer.custom_recognition("ZjcsPlaceholderReco")
class ZjcsPlaceholderReco(CustomRecognition):
    def analyze(
        self,
        context: Context,
        argv: CustomRecognition.AnalyzeArg,
    ) -> CustomRecognition.AnalyzeResult:
        return CustomRecognition.AnalyzeResult(
            box=(0, 0, 32, 32),
            detail=f"placeholder recognition: {argv.node_name}",
        )


@AgentServer.custom_action("ZjcsNoopAction")
class ZjcsNoopAction(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        print(f"[ZjcsNoopAction] node={argv.node_name}")
        return True


if __name__ == "__main__":
    main()
