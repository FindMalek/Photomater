from photoshop import Session

def find_layer_recursive(layer_set, target_path, current_path=[]):
    if not target_path:
        return None

    next_layer_name = target_path[1]
    for layer in layer_set.layers:
        new_path = current_path + [layer.name]
        if layer.name == next_layer_name:
            print(f" -> Found layer: {layer.typename}, ", len(target_path))
            if len(target_path) == 2:
                return layer
            
            elif layer.typename == 'LayerSet':
                return find_layer_recursive(layer, target_path[1:], current_path=new_path)
    
    return None

def main():
    # C:\Users\malek\Downloads\Daily Plan (Artboards).psd
    # psd_path = input("Enter the path to the PSD file: ").strip()
    psd_path = "C:/Users/malek/Downloads/Daily Plan (Artboards).psd"

    #layer_path_str = input("Enter the path to the target text layer (separated by '/'): ").strip()
    layer_path_str = "Dimanche/Date/Text/For texture/Date - Dimanche (EditText)"

    # Split the layer path into components
    layer_path = layer_path_str.split('/')

    with Session(psd_path, action="open") as ps:
        ps.echo(ps.active_document.name)
        artboards = ps.active_document.layerSets

        # Use a set for faster lookups
        target_artboards = {"Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"}

        # Iterate through each artboard and check if its name is in target_artboards
        for artboard in artboards:
            if artboard.name in target_artboards:
                print(f"Searching in artboard: {artboard.name}")
                target_layer = find_layer_recursive(artboard, layer_path)
                if target_layer and target_layer.kind == ps.LayerKind.TextLayer:
                    print(f" -> Found: {target_layer.name}, Text: {target_layer.textItem.contents}")
                    target_layer.textItem.contents = "00/00 "
                    break

if __name__ == '__main__':
    main()
