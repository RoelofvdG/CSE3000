package nl.roelofvdg.pdfsam_109;

public class ConsoleException extends Exception {

    public static final int ERR_ZERO_LENGTH = 0x01;
    public static final int CMD_LINE_HANDLER_NULL = 0x02;
    public static final int EMPTY_FILENAME = 0x03;
    public static final int CMD_LINE_VALIDATOR_NULL = 0x04;
    public static final int ERR_BAD_COMMAND = 0x05;
    public static final int CMD_LINE_EXECUTOR_NULL = 0x06;
    public static final int CMD_LINE_NULL = 0x07;
    public static final int PREFIX_REQUEST_NULL = 0x08;
    public static final int UNABLE_TO_RENAME = 0x09;
    public static final int UNABLE_TO_OVERWRITE = 0x0A;
    public static final int OVERWRITE_IS_FALSE = 0x0B;

    private static final long serialVersionUID = -853792961862291208L;

    public ConsoleException(final int exceptionErrorCode, final String[] args, final Throwable e) {
//        super(exceptionErrorCode, args, e);
    }

    public ConsoleException(final int exceptionErrorCode, final Throwable e) {
//        super(exceptionErrorCode, e);
    }

    public ConsoleException(final int exceptionErrorCode) {
//        super(exceptionErrorCode);
    }

    public ConsoleException(final Throwable e) {
        super(e);
    }

    public ConsoleException(final int exceptionErrorCode, final String[] args) {
//        super(exceptionErrorCode, args);
    }
}
