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
        # Loop through these artboards only: Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche (Dimanche may not exist in the PSD, sometimes it does and sometimes it doesn't)
        for artboard in artboards:
            if artboard.name in ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']:
                # Now search for the folders named 'Date' within these artboards and then search for the folder named 'For texture' within these folders you will find the text layers
                for layer in artboard.layers:
                    if layer.name == 'Date':
                        for layer in layer.layers:
                            if layer.name == 'Text':
                                print(layer)
                                for layer in layer.layers:
                                    if 'killoxs' in layer.name:
                                        print(layer)
                                        for layer in layer.layers:
                                            if layer.name == 'For texture':
                                                for layer in layer.layers:
                                                    if 'Date - ' in layer.name:
                                                        print(f"Found {layer.name}")


if __name__ == '__main__':
    main()
