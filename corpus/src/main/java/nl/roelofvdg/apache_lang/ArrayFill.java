package nl.roelofvdg.apache_lang;

import java.util.Arrays;

public final class ArrayFill {

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(byte[],byte)
     */
    public static byte[] fill(final byte[] a, final byte val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(char[],char)
     */
    public static char[] fill(final char[] a, final char val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(double[],double)
     */
    public static double[] fill(final double[] a, final double val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(float[],float)
     */
    public static float[] fill(final float[] a, final float val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(int[],int)
     */
    public static int[] fill(final int[] a, final int val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(long[],long)
     */
    public static long[] fill(final long[] a, final long val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(short[],short)
     */
    public static short[] fill(final short[] a, final short val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

    /**
     * Fills and returns the given array.
     *
     * @param <T> the array type.
     * @param a   the array to be filled (may be null).
     * @param val the value to be stored in all elements of the array.
     * @return the given array.
     * @see Arrays#fill(Object[],Object)
     */
    public static <T> T[] fill(final T[] a, final T val) {
        if (a != null) {
            Arrays.fill(a, val);
        }
        return a;
    }

}
