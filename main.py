from typing import TypedDict
from typing_extensions import Literal
from langgraph.graph import StateGraph, START, END
from IPython.display import display, Image

class State(TypedDict):
    name: str
    greeting: str

def hello_name(state: State):
    return {"greeting": f"Hello, {state['name']}"}

graph_builder = StateGraph(State)
graph_builder.add_node("hello_name", hello_name)
graph_builder.add_edge(START, "hello_name")
graph_builder.add_edge("hello_name", END)

graph = graph_builder.compile()


def main():
    print("Hello from langgraph-hello-world!")
    #img = Image(graph.get_graph().draw_mermaid_png())
    #display(img)

    resp = graph.invoke({"name": "Divya"})
    print(resp["greeting"])

if __name__ == "__main__":
    main()
