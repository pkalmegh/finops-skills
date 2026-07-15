# Evaluation Runner CLI

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Model-agnostic evaluation runner for FinOps Skills.")
    parser.add_argument("skill", nargs="?", help="Specify the skill ID to evaluate")
    parser.add_argument("--all", action="store_true", help="Run evaluations for all skills")
    parser.add_argument("--model", help="Target LLM model ID")
    
    args = parser.parse_args()
    print("FinOps Skills Evaluation Harness starting...")
    if args.all:
        print("Running all skills...")
    elif args.skill:
        print(f"Running skill: {args.skill}")
    else:
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
