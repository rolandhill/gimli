# -*- coding: utf-8 -*-
"""Matplotlib drawing functions used by `pygimli.viewer`."""

# are the following is suitable for a drawing package?
from .utils import (hold,
                    wait,
                    updateAxes,
                    saveFigure,
                    saveAxes,
                    adjustWorldAxes,
                    createAnimation,
                    saveAnimation,
                    setOutputStyle,
                    setPlotStuff)

from .boreholes import BoreHole, BoreHoles, create_legend

from .colorbar import (createColorBar,
                       createColorBarOnly,
                       findColorBar,
                       updateColorBar,
                       addCoverageAlpha,
                       autolevel,
                       cmapFromName,
                       findAndMaskBestClim,
                       setCbarLevels,
                       setMappableData)

from .meshview import (CellBrowser,
                       createMeshPatches,
                       createParameterContraintsLines,
                       createTriangles,
                       draw1DColumn,
                       drawField,
                       drawMesh,
                       drawMeshBoundaries,
                       drawModel,
                       drawMPLTri,
                       drawParameterConstraints,
                       drawPLC,
                       drawSelectedMeshBoundaries,
                       drawSelectedMeshBoundariesShadow,
                       drawSensors,
                       drawStreamLines,
                       drawStreams,
                       insertUnitAtNextLastTick,
                       plotLines)

from .overlayimage import (cacheFileName,
                           deg2MapTile,
                           getMapTile,
                           mapTile2deg,
                           underlayMap)

# TODO example scripts for the following and refactor is needed
# maybe ploter should named show or draw
from .dataview import (drawSensorAsMarker,  # dups to meshview??
                       generateMatrix,
                       patchMatrix,
                       patchValMap,
                       plotDataContainerAsMatrix,
                       plotMatrix,
                       plotVecMatrix)

from .modelview import (drawModel1D,
                        drawModel1DErr,
                        showmymatrix,  # backward compat, tbr
                        draw1dmodel,   # backward compat, tbr
                        show1dmodel,  # backward compat, tbr
                        draw1dmodelErr,  # backward compat, tbr
                        draw1dmodelLU,  # backward compat, tbr
                        showStitchedModels,
                        showStitchedModelsOld,
                        showStitchedModels_Redundant,
                        showfdemsounding,
                        insertUnitAtNextLastTick)


__all__ = [
    "BoreHole", "BoreHoles", "create_legend", "addCoverageAlpha", "autolevel",
    "cmapFromName",
    "createColorBar",
    "findColorBar",
    "updateColorBar",
    "findAndMaskBestClim", "setCbarLevels",
    "setMappableData", "drawSensorAsMarker", "generateMatrix", "patchMatrix",
    "patchValMap", "plotDataContainerAsMatrix", "plotMatrix", "plotVecMatrix",
    "CellBrowser", "createMeshPatches", "createParameterContraintsLines",
    "createTriangles", "draw1DColumn", "drawField", "drawMesh",
    "drawMeshBoundaries", "drawModel", "drawMPLTri", "hold", "wait",
    "setOutputStyle", "setPlotStuff", "createAnimation", "saveAnimation",
    "drawParameterConstraints", "drawPLC", "drawSelectedMeshBoundaries",
    "drawSelectedMeshBoundariesShadow", "drawSensors", "drawStreamLines",
    "drawStreams", "insertUnitAtNextLastTick", "plotLines", "cacheFileName",
    "deg2MapTile", "getMapTile", "mapTile2deg", "underlayMap", "updateAxes"
]


def createColorbar(*args, **kwargs):
    print("createColorbar is DEPRECATED .. please use createColorBar instead.")
    return createColorBar(*args, **kwargs)
