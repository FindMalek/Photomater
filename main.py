from photoshop import Session

def search_layers(layer_set, target_name):
    """
    Recursively searches for layers within a layer set.
    Prints the text of layers matching the target name format.
    """
    print(f"Searching {layer_set.name}...")
    for layer in layer_set.layers:
        # Check if layer is a group (layer set)
        if layer.typename == 'LayerSet':
            search_layers(layer, target_name)
        elif target_name in layer.name:
            try:
                if layer.kind == 'LayerKind.TEXT':
                    print(f"Layer: {layer.name}, Text: {layer.textItem.contents}")
            except AttributeError:
                # Not a text layer, ignore
                pass

def main():
    with Session(r"C:\Users\malek\Downloads\Daily Plan (Artboards).psd", action="open") as ps:
        ps.echo(ps.active_document.name)
        artboards = ps.active_document.layerSets

        for artboard in artboards:
            search_layers(artboard, 'Date - ')

if __name__ == '__main__':
    main()
