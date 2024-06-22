package nl.roelofvdg.jcvi_javacommon_92;

import org.junit.Test;

import static org.junit.Assert.*;

public class IlluminaUtilTest {

    private static final String ID = "SOLEXA1:4:1:12:1489#0/1";
    private static String NEW_ID = "SOLEXA3_0023_FC:4:8:17653:4072#TAGCTT/1";
    @Test
    public void instrumentName(){
        assertEquals("SOLEXA1", IlluminaUtil.getInstrumentName(ID));
        assertEquals("SOLEXA3", IlluminaUtil.getInstrumentName(NEW_ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForInsrumentNameShouldThrowNPE(){
        IlluminaUtil.getInstrumentName(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForInsrumentNameShouldThrowNPE(){
        IlluminaUtil.getInstrumentName("not an illumina id");
    }
    @Test
    public void flowCell(){
        assertEquals("4", IlluminaUtil.getFlowcellId(ID));
        assertEquals("4", IlluminaUtil.getFlowcellId(NEW_ID));
    }

    @Test(expected= NullPointerException.class)
    public void nullIdForFlowCellShouldThrowNPE(){
        IlluminaUtil.getFlowcellId(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForFlowCellShouldThrowNPE(){
        IlluminaUtil.getFlowcellId("not an illumina id");
    }
    @Test
    public void xClusterCoordinate(){
        assertEquals(12, IlluminaUtil.getXClusterCoordinate(ID));
        assertEquals(17653, IlluminaUtil.getXClusterCoordinate(NEW_ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForXClusterCoordinateShouldThrowNPE(){
        IlluminaUtil.getXClusterCoordinate(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForXClusterCoordinateShouldThrowNPE(){
        IlluminaUtil.getXClusterCoordinate("not an illumina id");
    }

    @Test
    public void yClusterCoordinate(){
        assertEquals(1489, IlluminaUtil.getYClusterCoordinate(ID));
        assertEquals(4072, IlluminaUtil.getYClusterCoordinate(NEW_ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForYClusterCoordinateShouldThrowNPE(){
        IlluminaUtil.getYClusterCoordinate(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForYClusterCoordinateShouldThrowNPE(){
        IlluminaUtil.getYClusterCoordinate("not an illumina id");
    }
    @Test
    public void multiplexIndex(){
        assertEquals(0, IlluminaUtil.getMultiplexIndex(ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForMultiplexIndexShouldThrowNPE(){
        IlluminaUtil.getMultiplexIndex(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForMultiplexIndexShouldThrowNPE(){
        IlluminaUtil.getMultiplexIndex("not an illumina id");
    }
    @Test
    public void pairNumber(){
        assertEquals(1, IlluminaUtil.getPairNumber(ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForPairNumberShouldThrowNPE(){
        IlluminaUtil.getPairNumber(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForPairNumberShouldThrowNPE(){
        IlluminaUtil.getPairNumber("not an illumina id");
    }

    @Test
    public void tileNumber(){
        assertEquals(1, IlluminaUtil.getTileNumber(ID));
    }
    @Test(expected= NullPointerException.class)
    public void nullIdForTileNumberShouldThrowNPE(){
        IlluminaUtil.getTileNumber(null);
    }
    @Test(expected= IllegalArgumentException.class)
    public void invalidIdForTileNumberShouldThrowNPE(){
        IlluminaUtil.getTileNumber("not an illumina id");
    }

}