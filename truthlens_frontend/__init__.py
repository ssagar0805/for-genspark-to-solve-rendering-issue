import streamlit.components.v1 as components
from pathlib import Path
import os

# Determine if we're in development mode
_RELEASE = not os.getenv("STREAMLIT_DEV_MODE", False)

if _RELEASE:
    # Production: serve the built React app
    _component_func = components.declare_component(
        "truthlens_frontend",
        path=str(Path(__file__).parent / "frontend" / "dist")
        # DON'T PUT WIDTH/HEIGHT HERE - it's not supported!
    )
else:
    # Development: use Vite dev server
    _component_func = components.declare_component(
        "truthlens_frontend", 
        url="http://localhost:5173"  # Vite default dev server port
        # DON'T PUT WIDTH/HEIGHT HERE - it's not supported!
    )

def render_truthlens_app(key=None, width=1400, height=1000, **props):
    """
    Render the complete TruthLens React frontend as a Streamlit component.
    
    Parameters:
    - key: Streamlit component key for state management
    - width: Component width in pixels (default: 1400)
    - height: Component height in pixels (default: 1000)
    - **props: Any data to pass to the React frontend
    
    Returns:
    - Component return value (data from React to Python)
    """
    return _component_func(
        key=key,
        width=width,   # Width goes HERE when calling the component
        height=height, # Height goes HERE when calling the component
        default=None,
        **props
    )

# Convenience alias
render_app = render_truthlens_app
