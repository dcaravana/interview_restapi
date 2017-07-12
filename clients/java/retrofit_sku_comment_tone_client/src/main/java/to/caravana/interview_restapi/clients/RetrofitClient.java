package to.caravana.interview_restapi.clients;

import java.io.IOException;
import java.util.List;
import okhttp3.Authenticator;
import okhttp3.Credentials;
import okhttp3.Interceptor;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Route;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.Retrofit;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;


public final class RetrofitClient {
  private final String API_URL = "http://127.0.0.1:8000";

  private Retrofit retrofit;
  private SkuCommentTone skuCommentTone;

  public RetrofitClient() {

    // quite crazy apparently, that's just for HTTP basic auth
    OkHttpClient client = new OkHttpClient.Builder()
        .addInterceptor(new Interceptor() {
            @Override public okhttp3.Response intercept(Interceptor.Chain chain) throws IOException {
                Request request = chain.request();
                String credential = Credentials.basic("admin", "admin001");
                Request newReq = request.newBuilder()
                    .addHeader("Authorization", credential)
                    .build();
                okhttp3.Response response = chain.proceed(newReq);
                return response;
            }
        })
        .build();

    retrofit = new Retrofit.Builder()
        .baseUrl(API_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .client(client)
        .build();

    skuCommentTone = retrofit.create(SkuCommentTone.class);
  }

  public static class Comment {
    public final int id;
    public final String sku;
    public final String content;
    public final String tone;
    public final Boolean tone_is_positive;

    public Comment(int id, String sku, String content, String tone, Boolean tone_is_positive) {
      this.id = id;
      this.sku = sku;
      this.content = content;
      this.tone = tone;
      this.tone_is_positive = tone_is_positive;
    }

    public Comment(String sku, String content) {
      this.id = 0;
      this.sku = sku;
      this.content = content;
      this.tone = null;
      this.tone_is_positive = false;
    }
  }

  public interface SkuCommentTone {
    @GET("comments")
    Call<List<Comment>> comments();
    @GET("comments/{id}")
    Call<Comment> comment(@Path("id") int id);
    @POST("comments/")
    Call<Comment> createComment(@Body Comment comment);
  }

  public List<Comment> getComments() throws IOException {
    Call<List<Comment>> call = skuCommentTone.comments();
    return call.execute().body();
  }

  public Comment getComment(int id) throws IOException {
    Call<Comment> call = skuCommentTone.comment(id);
    return call.execute().body();
  }

  public Comment createComment(Comment comment) throws IOException {
    Call<Comment> call = skuCommentTone.createComment(comment);
    Response<Comment> response = call.execute();
    return response.body();
  }
}
