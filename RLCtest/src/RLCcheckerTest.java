import java.io.FileReader;
import java.io.Reader;
import java.io.Closeable;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.zip.ZipFile;
// import org.checkerframework.framework.qual.*;
// import org.checkerframework.checker.mustcall.qual.*;
// import org.checkerframework.checker.calledmethods.qual.*;

class RLCcheckerTest {
    public static void main(String[] args) {
        try {
            ZipfileMojoReaderBackend zfwrap = new ZipfileMojoReaderBackend("archive");
            zfwrap.close();
        } catch (Exception ex) {
        }
    }
}

// @MustCall("close")
class ZipfileMojoReaderBackend implements Closeable {
  // private final @Owning ZipFile zf;
  private final ZipFile zf;
 
  public ZipfileMojoReaderBackend(String archivename) throws IOException {
    zf = new ZipFile(archivename);
  }

  // @Override
  // @EnsuresCalledMethods(value="zf", methods="close")
  public void close() throws IOException {
    zf.close();
    // if (zf != null) {
    //   ZipFile f = zf;
    //   // zf = null;
    //   f.close();
    // }
  }
}
