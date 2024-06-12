package nl.roelofvdg.apache_lang;

import org.junit.Test;

import static org.junit.Assert.*;

public class ArrayFillTest {

    @Test
    public void testFillByteArray() {
        final byte[] array = new byte[3];
        final byte val = (byte) 1;
        final byte[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final byte v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillByteArrayNull() {
        final byte[] array = null;
        final byte val = (byte) 1;
        final byte[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillCharArray() {
        final char[] array = new char[3];
        final char val = 1;
        final char[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final char v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillCharArrayNull() {
        final char[] array = null;
        final char val = 1;
        final char[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillDoubleArray() {
        final double[] array = new double[3];
        final double val = 1;
        final double[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final double v : actual) {
            assertEquals(val, v, 0.f);
        }
    }

    @Test
    public void testFillDoubleArrayNull() {
        final double[] array = null;
        final double val = 1;
        final double[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillFloatArray() {
        final float[] array = new float[3];
        final float val = 1;
        final float[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final float v : actual) {
            assertEquals(val, v, 0.f);
        }
    }

    @Test
    public void testFillFloatArrayNull() {
        final float[] array = null;
        final float val = 1;
        final float[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillIntArray() {
        final int[] array = new int[3];
        final int val = 1;
        final int[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final int v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillIntArrayNull() {
        final int[] array = null;
        final int val = 1;
        final int[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillLongArray() {
        final long[] array = new long[3];
        final long val = 1;
        final long[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final long v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillLongArrayNull() {
        final long[] array = null;
        final long val = 1;
        final long[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillObjectArray() {
        final String[] array = new String[3];
        final String val = "A";
        final String[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final String v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillObjectArrayNull() {
        final Object[] array = null;
        final Object val = 1;
        final Object[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }

    @Test
    public void testFillShortArray() {
        final short[] array = new short[3];
        final short val = (byte) 1;
        final short[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
        for (final short v : actual) {
            assertEquals(val, v);
        }
    }

    @Test
    public void testFillShortArrayNull() {
        final short[] array = null;
        final short val = 1;
        final short[] actual = ArrayFill.fill(array, val);
        assertSame(array, actual);
    }
}