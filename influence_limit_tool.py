WINDOW_NAME = "Influence_Limit_Tool"

def select_verts_with_too_many_influences(mesh: str, cluster: str, max_influences: str, *args):

    # Parse max_influences as int
    max_influences_int = 0
    try:
        max_influences_int = int(max_influences)
    except Exception as e:
        print(f"Unable to parse max influences as int")
        print(e)
        return


    # Grab all verts in provided mesh
    try:
        verts=cmds.polyEvaluate(mesh , v=True)
    except Exception as e:
        print(f"Unable to retrieve verts from provided mesh name {mesh})")
        print(e)
        return

    try:
        for i in range(verts):

            vert_list_query = f'{mesh}.vtx[{i}]'
            
            # Use skinPercent cmd to extract all influences on current vert
            vert_influences = cmds.skinPercent(cluster, vert_list_query, q=True, value=True) 

            # Calculate the number of influences
            num_influences = len([influence for influence in vert_influences if influence > 0]) 

            # Select vert if the influence is over max 
            if (num_influences > max_influences_int ):
                cmds.select(vert_list_query, add=True)
    except Exception as e:
        print(f"Unable to retrieve and evaluate number of influences from verts")
        print(e)
        return

def create_gui():
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    window = cmds.window(WINDOW_NAME, title=WINDOW_NAME, width=200)

    layout = cmds.columnLayout()
    # Create first text input
    cmds.text(label="Mesh Name:")
    mesh_field = cmds.textField()
    
    # Create second text input
    cmds.text(label="Cluster Name:")
    cluster_field = cmds.textField()

    cmds.text(label="Max Num Influences")
    max_influence_field = cmds.textField()
    
    # Create button
    cmds.button(label="Check for Violations", command=lambda x: select_verts_with_too_many_influences(
        cmds.textField(mesh_field, query=True, text=True), 
        cmds.textField(cluster_field, query=True, text=True), 
        cmds.textField(max_influence_field, query=True, text=True) 
    ))
    
    # Show the window
    cmds.showWindow(window)


create_gui()
