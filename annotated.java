import java.io.FileReader;
import java.io.Reader;
import java.io.Closeable;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.zip.ZipFile;

// import org.checkerframework.framework.qual.*;
// import org.checkerframework.checker.mustcall.qual.*;
// import org.checkerframework.checker.calledmethods.qual.*;
@org.checkerframework.framework.qual.AnnotatedFor("org.checkerframework.checker.resourceleak.ResourceLeakChecker")
class RLCcheckerTest {

    @org.checkerframework.dataflow.qual.Impure
    public static void main(String[] args) {
        try {
            ZipfileMojoReaderBackend zfwrap = new ZipfileMojoReaderBackend("archive");
            zfwrap.close();
        } catch (Exception ex) {
        }
    }
}

@org.checkerframework.framework.qual.AnnotatedFor("org.checkerframework.checker.resourceleak.ResourceLeakChecker")
@org.checkerframework.checker.mustcall.qual.InheritableMustCall({ "close" })
class ZipfileMojoReaderBackend implements Closeable {

    @org.checkerframework.checker.mustcall.qual.Owning
    private final ZipFile zf;

    @org.checkerframework.dataflow.qual.Impure
    public ZipfileMojoReaderBackend(String archivename) throws IOException {
        zf = new ZipFile(archivename);
    }

    @org.checkerframework.checker.calledmethods.qual.EnsuresCalledMethods(value = { "this.zf" }, methods = { "close" })
    @org.checkerframework.dataflow.qual.Impure
    public void close() throws IOException {
        zf.close();
    }
}
