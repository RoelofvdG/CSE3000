package nl.roelofvdg.liferay_108;

import java.io.IOException;
import java.io.InputStream;

public class UnsyncBufferedInputStream {
    public UnsyncBufferedInputStream(InputStream inputStream) {
        this(inputStream, _DEFAULT_BUFFER_SIZE);
    }

    public InputStream inputStream;
    protected byte[] buffer;
    protected int firstInvalidIndex;
    protected int index;
    protected int markLimitIndex = -1;

    private static final int _DEFAULT_BUFFER_SIZE = 8192;

    public UnsyncBufferedInputStream(InputStream inputStream, int size) {
        this.inputStream = inputStream;
        if (size <= 0) {
            throw new IllegalArgumentException("Size is less than 0");
        }

        buffer = new byte[size];
    }

    public int available() throws IOException {
        if (inputStream == null) {
            throw new IOException("Input stream is null");
        }

        return inputStream.available() + (firstInvalidIndex - index);
    }


    public void close() throws IOException {
        if (inputStream != null) {
            inputStream.close();

            inputStream = null;
            buffer = null;
        }
    }


    public void mark(int readLimit) {
        if (readLimit <= 0) {
            return;
        }

        markLimitIndex = readLimit;

        if (index > 0) {

            int available = firstInvalidIndex - index;

            if (available > 0) {

                // Shuffle mark beginning to buffer beginning

                System.arraycopy(buffer, index, buffer, 0, available);

                index = 0;

                firstInvalidIndex = available;
            }
            else {

                // Reset buffer states

                index = firstInvalidIndex = 0;
            }
        }
    }


    public boolean markSupported() {
        return true;
    }


    public int read() throws IOException {
        if (inputStream == null) {
            throw new IOException("Input stream is null");
        }

        if (index >= firstInvalidIndex) {
            fillInBuffer();

            if (index >= firstInvalidIndex) {
                return -1;
            }
        }

        return buffer[index++] & 0xff;
    }


    public int read(byte[] bytes) throws IOException {
        return read(bytes, 0, bytes.length);
    }


    public int read(byte[] bytes, int offset, int length) throws IOException {
        if (inputStream == null) {
            throw new IOException("Input stream is null");
        }

        if (length <= 0) {
            return 0;
        }

        int read = 0;

        while (true) {

            // Try to at least read some data

            int currentRead = readOnce(bytes, offset + read, length - read);

            if (currentRead <= 0) {
                if (read == 0) {
                    read = currentRead;
                }

                break;
            }

            read += currentRead;

            if ((read >= length) || (inputStream.available() <= 0)) {

                // Read enough or further reading may be blocked, stop reading

                break;
            }
        }

        return read;
    }


    public void reset() throws IOException {
        if (inputStream == null) {
            throw new IOException("Input stream is null");
        }

        if (markLimitIndex < 0) {
            throw new IOException("Resetting to invalid mark");
        }

        index = 0;
    }


    public long skip(long skip) throws IOException {
        if (inputStream == null) {
            throw new IOException("Input stream is null");
        }

        if (skip <= 0) {
            return 0;
        }

        long available = firstInvalidIndex - index;

        if (available <= 0) {
            if (markLimitIndex < 0) {

                // No mark required, skip the underlying input stream

                return inputStream.skip(skip);
            }
            else {

                // Mark required, save the skipped data

                fillInBuffer();

                available = firstInvalidIndex - index;

                if (available <= 0) {
                    return 0;
                }
            }
        }

        // Skip the data in buffer

        if (available < skip) {
            skip = available;
        }

        index += skip;

        return skip;
    }

    protected void fillInBuffer() throws IOException {
        if (markLimitIndex < 0) {

            // No mark required, fill the buffer

            index = firstInvalidIndex = 0;

            int number = inputStream.read(buffer);

            if (number > 0) {
                firstInvalidIndex = number;
            }

            return;
        }

        // Mark required

        if (index >= markLimitIndex) {

            // Passed mark limit indexs, get rid of all cache data

            markLimitIndex = -1;

            index = firstInvalidIndex = 0;
        }
        else if (index == buffer.length) {

            // Cannot get rid of cache data and there is no room to read in any
            // more data, so grow the buffer

            int newBufferSize = buffer.length * 2;

            if (newBufferSize > markLimitIndex) {
                newBufferSize = markLimitIndex;
            }

            byte[] newBuffer = new byte[newBufferSize];

            System.arraycopy(buffer, 0, newBuffer, 0, buffer.length);

            buffer = newBuffer;
        }

        // Read underlying input stream since the buffer has more space

        firstInvalidIndex = index;

        int number = inputStream.read(buffer, index, buffer.length - index);

        if (number > 0) {
            firstInvalidIndex += number;
        }
    }

    protected int readOnce(byte[] bytes, int offset, int length)
            throws IOException {

        int available = firstInvalidIndex - index;

        if (available <= 0) {

            // Buffer is empty, read from under input stream

            if ((markLimitIndex < 0) && (length >= buffer.length)) {

                // No mark required, left read block is no less than buffer,
                // read through buffer is inefficient, so directly read from
                // underlying input stream

                return inputStream.read(bytes, offset, length);
            }
            else {

                // Mark is required, has to read through the buffer to remember
                // data

                fillInBuffer();

                available = firstInvalidIndex - index;

                if (available <= 0) {
                    return -1;
                }
            }
        }

        if (length > available) {
            length = available;
        }

        System.arraycopy(buffer, index, bytes, offset, length);

        index += length;

        return length;
    }
}