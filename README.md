# Maya-Influence-Limit-Tool
A Python utility for Autodesk Maya that identifies and selects vertices exceeding a specified bone influence limit. Essential for game development pipelines where vertex influence counts must be controlled for performance.

##  Purpose

Game engines often have strict limits on how many bones can influence a single vertex (typically 4 influences). This tool helps technical artists quickly find and fix vertices that violate these constraints before export.

## Requirements

- **Maya**: 2018 or newer
- **Python**: 2.7+ (Maya 2018-2022) or 3.x (Maya 2023+)
- **Dependencies**: None (uses built-in Maya commands)

##  Installation

1. Save the script as `influence_limit_tool.py` (no need to clone repo)
2. Place it in your Maya scripts directory:
3. Restart Maya then open the Script Editor
```python
   import influence_limit_tool
   influence_limit_tool.create_gui()
```
4. Paste this code in a Python tab:
```python
   import influence_limit_tool
   influence_limit_tool.create_gui()
```
5. Middle-mouse drag the code to your shelf
6. Click the new shelf button anytime to launch the tool

### Example
```
Mesh Name: character_mesh
Cluster Name: skinCluster1
Max Num Influences: 4
```

Click "Check for Violations" → All vertices with 5+ influences are now selected


### Finding Your Cluster Name

If you don't know your skinCluster name:

1. Select your mesh
2. Go to **Windows → Hypergraph: Connections**
3. Look for the node named `skinCluster` followed by a number

Or run this in the Script Editor:
```python
import maya.cmds as cmds
cmds.ls(type='skinCluster')
```

## Troubleshooting

**Issue**: "Unable to retrieve verts from provided mesh name"
- **Solution**: Check mesh name spelling (case-sensitive)
- **Solution**: Ensure the mesh exists in the scene

**Issue**: "Unable to parse max influences as int"
- **Solution**: Enter only numbers (e.g., `4`, not `four`)

**Issue**: "Unable to retrieve and evaluate number of influences"
- **Solution**: Verify the cluster name is correct
- **Solution**: Ensure the mesh is actually skinned to the cluster

**Issue**: No vertices selected but I know there are violations
- **Solution**: Make sure you're checking the correct mesh/cluster pair
- **Solution**: Try a lower max influence number
  
## Known Limitations

- Only works with skinCluster deformers
- Processes one mesh at a time
- Does not automatically fix violations (only selects them)
- Requires exact mesh and cluster names (no fuzzy matching)
