from IPython.display import Image, display

def display_graph(graph , filename="graph.png"):
    try:
        image_data = graph.get_graph().draw_mermaid_png()

        # Handle both bytes or file-like object (e.g. BytesIO)
        if hasattr(image_data, 'read'):
            content = image_data.read()
        else:
            content = image_data

        with open(filename, "wb") as f:
            f.write(content)

        print(f"Graph image saved as {filename}")
    except Exception as e:
        print(f"Error saving graph: {e}")
