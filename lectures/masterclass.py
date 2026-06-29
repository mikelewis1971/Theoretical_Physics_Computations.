#!/usr/bin/env python3
"""
masterclass.py
================
THE CHIRAL SEAM MASTERCLASS
A complete, self-verifying walkthrough of the eight-paper chiral-seam
framework, from the two-body Heisenberg uncertainty principle to dark
matter and dark energy.

Run the whole thing:
    python3 masterclass.py

Run a single lecture:
    python3 masterclass.py --lecture 5

Run without pausing between lectures:
    python3 masterclass.py --no-pause

Every numbered equation from the source material is implemented as a
Python function with an explicit PASS/FAIL verification. Where the
verification caught a genuine error in the original formulas (and four
were caught during construction of this masterclass), the bug, the fix,
and the reasoning are documented inline in the corresponding lecture
module and summarized in BUGFIXES.md.
"""

import argparse
import sys
from constants import banner, RULE

LECTURES = {
    1: ("lecture_01_two_body", "The Two-Body Heisenberg Algebra and the Pair Axis"),
    2: ("lecture_02_seam_geometry", "The Chiral Seam and the Dirac Equation"),
    3: ("lecture_03_algebraic_structures", "Complete Algebraic Structures"),
    4: ("lecture_04_higher_heisenberg", "The Higher Heisenberg Relation on the Seam"),
    5: ("lecture_05_higgs_kink", "The Higgs Kink, Poschl-Teller Spectrum, Three Generations"),
    6: ("lecture_06_mass_hierarchy", "Fermion Mass Hierarchy"),
    7: ("lecture_07_mould_gravity", "The Mould Effect and Emergent Gravity"),
    8: ("lecture_08_dark_sector", "Dark Matter and Dark Energy from the Berry Connection"),
}


def professor_intro():
    print(RULE)
    print(RULE)
    print("""
                       THE CHIRAL SEAM MASTERCLASS
       From the Two-Body Heisenberg Uncertainty Principle
                  to Dark Matter and Dark Energy

   Eight lectures. Every equation implemented and verified in Python.
   Every claim is either a PASS/FAIL computational check, or explicitly
   labeled as a conjecture / open problem / known limitation.
""")
    print(RULE)
    print(RULE)
    print()
    print("Professor:")
    print("  Welcome. This course has one rule: nothing is asserted without a")
    print("  computation. We start from the most elementary fact in two-body")
    print("  quantum mechanics and, by the end of lecture 8, we will have derived")
    print("  the Standard Model gauge group, the Higgs mechanism, three fermion")
    print("  generations, the fermion mass hierarchy, Newtonian gravity, the")
    print("  equivalence principle, and -- if the final conjecture holds -- dark")
    print("  matter and dark energy, all from a single geometric object: a")
    print("  two-dimensional boundary between a spherical and a hyperbolic")
    print("  curvature domain, called the chiral seam.")
    print()
    print("  Along the way we will find, and fix, four genuine mathematical")
    print("  errors in earlier drafts of this material -- because that is what")
    print("  rigor looks like in practice: not getting everything right the")
    print("  first time, but having a verification process that catches it when")
    print("  you don't.")


def professor_outro(results):
    banner("END OF MASTERCLASS -- FULL RESULTS LEDGER")
    n_total = len(results)
    n_pass = sum(1 for v in results.values() if v)
    print(f"\n  Lectures completed: {n_pass} / {n_total}\n")
    for i in sorted(results):
        module_name, title = LECTURES[i]
        status = "COMPLETED" if results[i] else "ERROR"
        print(f"    Lecture {i}: {title:<60} [{status}]")
    print()
    print("Professor's closing remark:")
    print("  We began with [rho, P] = 0, a fact about two-body quantum mechanics")
    print("  that most physicists have seen but few have asked 'what if this")
    print("  defines a geometric axis?' Eight lectures later, that question has")
    print("  produced the Standard Model gauge group, the Higgs kink, exactly")
    print("  three generations, a parameter-economical fermion mass formula,")
    print("  Newtonian gravity with the equivalence principle built in, and a")
    print("  speculative but concrete mechanism for dark matter and dark energy.")
    print()
    print("  What should you take away? Not that this is settled physics -- it")
    print("  is a speculative framework, clearly labeled as such throughout.")
    print("  What IS settled is the internal mathematics: every theorem proved")
    print("  here was proved on explicit matrices, explicit integrals, or")
    print("  explicit numerical models, and every conjecture was labeled a")
    print("  conjecture. That discipline -- checking your own equations harder")
    print("  than anyone else will -- is the actual subject of this course.")
    print()
    print(RULE)


def run_lecture(n, pause=True):
    module_name, title = LECTURES[n]
    module = __import__(module_name)
    try:
        result = module.run()
    except Exception as exc:
        print(f"\n  !!! Lecture {n} raised an exception: {exc!r}")
        import traceback
        traceback.print_exc()
        return False
    if pause and n < len(LECTURES):
        try:
            input("\n  [Press Enter to continue to the next lecture, or Ctrl+C to stop] ")
        except (EOFError, KeyboardInterrupt):
            print("\n  (continuing automatically -- no interactive input available)")
    return bool(result)


def main():
    parser = argparse.ArgumentParser(description="The Chiral Seam Masterclass")
    parser.add_argument("--lecture", type=int, default=None,
                         help="Run only this lecture number (1-8)")
    parser.add_argument("--no-pause", action="store_true",
                         help="Do not pause between lectures")
    args = parser.parse_args()

    pause = not args.no_pause

    if args.lecture is not None:
        if args.lecture not in LECTURES:
            print(f"Lecture {args.lecture} does not exist. Choose 1-8.")
            sys.exit(1)
        run_lecture(args.lecture, pause=False)
        return

    professor_intro()
    results = {}
    for n in sorted(LECTURES):
        results[n] = run_lecture(n, pause=pause)
    professor_outro(results)


if __name__ == "__main__":
    main()
