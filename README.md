Floor Level Projects (Python CLI Applications)

Welcome to my repository featuring foundational Python applications. 
These projects were developed during the early stages of my transition into the tech industry. 
They demonstrate my practical understanding of core programming concepts, data structures, error handling, and terminal-based User Experience (UX).

Core Programming Skills Demonstrated

Through this repository, I have proven proficiency in:
- Error & Exception Handling: Anticipating edge cases and user entry mistakes using `try-except` blocks.
- Data Structures: Working comfortably with `lists`, `tuples`, and `dictionaries`.
- Control Flow Mastery: Writing clean loop structures (`while`, `for`) and conditional logic gates.

!!! Language Note: !!! The codebase and internal logic are fully documented/structured in English, while the interactive command-line interface prompts communicate with the user in Polish.

Projects Overview & Technical Highlights

1. Multi-Functional Calculator (`kalkulator`)
A robust, console-based calculator that performs arithmetic operations within an infinite deployment loop.
- Technical Features:
    - Data Validation: Utilizes nested `while True` loops paired with `try-except` blocks to catch `ValueError` exceptions, ensuring only integers are accepted,
    - Defensive Programming: Implements custom validation to prevent zero-division errors (`ZeroDivisionError`) with a user-friendly warning,
    - State Management: Features a dynamic closure prompt allowing the user to seamlessly continue or safely exit the application using `exit()`,

2. Rock, Paper, Scissors Game (`gra-papier-kamien-nozyce`)
A automated, multi-round battle script where the user plays against an AI opponent.
- Technical Features:
    - Pacing & UX: Implements Python's `time` module (`time.sleep`) to simulate game pacing and data aggregation processing ("Zliczanie głosów..."),
    - Randomization: Employs `random.choice` to execute unpredictable AI moves from a pre-defined tuple,
    - Complex Control Flow: Features structured, multi-line conditional statements to evaluate win/loss/tie matrices and accurately track cross-round score states,

3. Interactive Quiz Application (`quiz`)
A complete, map-driven quiz game that dynamically pulls random questions from a pool and validates cumulative performance.
- Technical Features:
    - Advanced Data Mapping: Uses a dictionary (`answer_map`) to efficiently map character inputs (`a`, `b`, `c`, `d`) to numerical index positions for answer verification,
    - Dynamic Data Pools: Leverages standard list methods (`.remove()`) to extract used elements on-the-fly, ensuring questions are never repeated within the same session,
    - Modular Architecture: Separates execution logic into a clean `quiz()` function invoked by a main state controller,

