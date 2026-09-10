import sys
import json
from client import HilbertTransformEngine

def main():
    engine = HilbertTransformEngine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "analytic_signal":
            _, env, phase = engine.analytic_signal(params.get("signal", []))
            res = {"envelope": env, "phase": phase}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
