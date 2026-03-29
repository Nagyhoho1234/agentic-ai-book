"""
Gradio Equation Plotter & Solver
================================
Enter a mathematical equation, adjust parameters, see the plot instantly.
Run: python 02_equation_solver.py

Demonstrates how scientists can wrap their models in a web interface
that colleagues can use without understanding the code.
"""

import gradio as gr
import numpy as np
import matplotlib.pyplot as plt


def solve_and_plot(equation_str, x_min, x_max, num_points, param_a, param_b, param_c):
    """Parse and plot a mathematical equation with parameters a, b, c."""
    x = np.linspace(x_min, x_max, int(num_points))

    # Make parameters available in the equation namespace
    a, b, c = param_a, param_b, param_c

    try:
        # Evaluate the equation string safely
        # Users can use: x, a, b, c, np functions (sin, cos, exp, log, sqrt, pi, e)
        safe_dict = {
            "x": x, "a": a, "b": b, "c": c,
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "log10": np.log10,
            "sqrt": np.sqrt, "abs": np.abs,
            "pi": np.pi, "e": np.e,
            "np": np,
        }
        y = eval(equation_str, {"__builtins__": {}}, safe_dict)

        # Create publication-quality figure
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y, "b-", linewidth=2)
        ax.set_xlabel("x", fontsize=14)
        ax.set_ylabel("f(x)", fontsize=14)
        ax.set_title(f"f(x) = {equation_str}", fontsize=16)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color="k", linewidth=0.5)
        ax.axvline(x=0, color="k", linewidth=0.5)
        plt.tight_layout()

        # Compute basic properties
        y_finite = y[np.isfinite(y)]
        info = f"""**Equation:** f(x) = {equation_str}
**Parameters:** a={a}, b={b}, c={c}
**Domain:** [{x_min}, {x_max}], {int(num_points)} points
**Range:** [{y_finite.min():.4f}, {y_finite.max():.4f}]
**Mean:** {y_finite.mean():.4f}
**Std:** {y_finite.std():.4f}"""

        # Find zeros (sign changes)
        sign_changes = np.where(np.diff(np.sign(y)))[0]
        if len(sign_changes) > 0:
            zeros = [f"{x[i]:.4f}" for i in sign_changes[:10]]
            info += f"\n**Approximate zeros:** {', '.join(zeros)}"

        return fig, info

    except Exception as e:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"Error: {str(e)}", ha="center", va="center",
                fontsize=14, color="red", transform=ax.transAxes)
        return fig, f"**Error:** {str(e)}"


# Build the Gradio interface
demo = gr.Interface(
    fn=solve_and_plot,
    inputs=[
        gr.Textbox(
            value="a * sin(b * x) + c",
            label="Equation (use x, a, b, c, sin, cos, exp, log, sqrt, pi, e)",
        ),
        gr.Slider(-20, 0, value=-10, label="x min"),
        gr.Slider(0, 20, value=10, label="x max"),
        gr.Slider(50, 2000, value=500, step=50, label="Number of points"),
        gr.Slider(-10, 10, value=1, step=0.1, label="Parameter a"),
        gr.Slider(-10, 10, value=2, step=0.1, label="Parameter b"),
        gr.Slider(-10, 10, value=0, step=0.1, label="Parameter c"),
    ],
    outputs=[
        gr.Plot(label="Plot"),
        gr.Markdown(label="Properties"),
    ],
    title="Equation Plotter & Solver",
    description="Enter any mathematical equation and adjust parameters interactively. "
                "Useful for exploring model behavior, teaching, and presentations.",
    examples=[
        ["a * x**2 + b * x + c", -5, 5, 500, 1, -2, -3],
        ["a * exp(-b * x**2)", -5, 5, 500, 1, 0.5, 0],
        ["a * sin(b * x) * exp(-c * abs(x))", -10, 10, 1000, 1, 3, 0.1],
        ["a / (1 + exp(-b * (x - c)))", -10, 10, 500, 1, 1, 0],
        ["a * x**3 - b * x + c", -3, 3, 500, 1, 3, 0],
    ],
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()
