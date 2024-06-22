package nl.roelofvdg.jcvi_javacommon_92;

import junit.framework.TestCase;
import org.junit.Test;
import static org.junit.Assert.*;

public class DistanceTest {
    float mean = 3.14F;
    float stdDev = 0.5F;

    Distance sut = Distance.buildDistance(mean, stdDev);

    public static void assertEqualAndHashcodeSame(Object obj1, Object obj2) {
        assertEquals(obj1, obj2);
        assertTrue(obj1.hashCode()== obj2.hashCode());

        assertEquals(obj2,obj1);
        assertTrue(obj2.hashCode()== obj1.hashCode());
    }

    public static void assertNotEqualAndHashcodeDifferent(Object obj1,Object obj2) {
        assertFalse(obj1.equals(obj2));
        assertFalse(obj1.hashCode()== obj2.hashCode());

        assertFalse(obj2 + " vs " + obj1, obj2.equals(obj1));
        assertFalse(obj2.hashCode()== obj1.hashCode());
    }

    @Test
    public void constructor(){
        assertEquals(mean, sut.getMean(),0);
        assertEquals(stdDev, sut.getStdDev(),0);
    }

    @Test
    public void equalsSameRef(){
        assertEqualAndHashcodeSame(sut, sut);
    }

    @Test
    public void equalsSameValues(){
        Distance sameValues = Distance.buildDistance(mean, stdDev);
        assertEqualAndHashcodeSame(sut, sameValues);
    }

    @Test
    public void notEqualsNull(){
        assertFalse(sut.equals(null));
    }
    @Test
    public void notEqualsDifferentClass(){
        assertFalse(sut.equals("Not a Distance"));
    }
    @Test
    public void differentMeanShouldNotBeEqual(){
        Distance differentMean = Distance.buildDistance(mean-1, stdDev);
        assertNotEqualAndHashcodeDifferent(sut, differentMean);
    }
    @Test
    public void differentStdDevShouldNotBeEqual(){
        Distance differentStdDev = Distance.buildDistance(mean, stdDev - 0.25F);
        assertNotEqualAndHashcodeDifferent(sut, differentStdDev);
    }

    @Test
    public void buildDistance(){
        Distance actual = Distance.buildDistance(0, 10);
        Distance expected = Distance.buildDistance(5F, 10/6F);
        assertEquals(expected, actual);
    }
    @Test
    public void buildDistanceIntMaxDoesntOverflow(){
        Distance actual = Distance.buildDistance(Integer.MAX_VALUE-1, Integer.MAX_VALUE);
        Distance expected = Distance.buildDistance(Integer.MAX_VALUE-1, Integer.MAX_VALUE,2147483646.5F, 1/6F);
        assertEquals(expected, actual);
    }

    @Test
    public void distanceWhere3StdDevsIsZero(){
        Distance actual = Distance.buildDistance(0, 300);
        Distance expected = Distance.buildDistance(150F, 50F);
        assertEquals(expected, actual);
    }
    @Test
    public void transformCeleraAssemblerDistanceChangesStdIfMeanIsLessthan3StdDevs(){
        float mean =(stdDev*3) -1;
        Distance original = Distance.buildDistance(mean, stdDev);
        Distance actual = Distance.transformIntoCeleraAssemblerDistance(original);
        Distance expected = Distance.buildDistance(original.getMin(), original.getMax(),
                mean, (mean-1.015F)/3);
        assertEquals(expected, actual);
    }
    @Test
    public void transformCeleraAssemblerDistanceDoNotChangeIfMeanIsMorethan3StdDevs(){
        float mean =(stdDev*3);
        Distance original = Distance.buildDistance(mean, stdDev);
        Distance actual = Distance.transformIntoCeleraAssemblerDistance(original);
        assertSame(original, actual);
    }
}