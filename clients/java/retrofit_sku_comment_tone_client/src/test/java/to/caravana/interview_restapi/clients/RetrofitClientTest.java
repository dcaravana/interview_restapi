package to.caravana.interview_restapi.clients;

import java.io.IOException;
import java.util.List;
import java.util.UUID;
import org.junit.Test;
import static org.junit.Assert.*;
import to.caravana.interview_restapi.clients.*;


public class RetrofitClientTest {

  private String username = "admin", password = "admin001";

  @Test public void testCreateComment() {
    RetrofitClient classUnderTest = new RetrofitClient(username, password);
    RetrofitClient.Comment comment = new RetrofitClient.Comment(
      UUID.randomUUID().toString(),
      "This is a good message that makes me content.");
    comment = classUnderTest.createComment(comment);
    assertTrue("createComment() should create a new comment having positive tone",
      comment.tone_is_positive);
  }

  @Test public void testGetComment() {
    RetrofitClient classUnderTest = new RetrofitClient(username, password);
    RetrofitClient.Comment comment = classUnderTest.getComment(1);
    assertTrue("getComment() should return comment id 1", comment.id == 1);
  }

  @Test public void testGetComments() {
    RetrofitClient classUnderTest = new RetrofitClient(username, password);
    List<RetrofitClient.Comment> comments = classUnderTest.getComments();
    assertTrue("getComments() size should be > 0", comments.size() > 0);
  }

}
