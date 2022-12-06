package com.example.interview.crawler;

import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import java.util.*;
import java.util.concurrent.*;

@Component
@Scope("prototype")
public class WebCrawler {
    private final Queue<String> urlQueue = new ConcurrentLinkedQueue<>();
    private final Map<String, Boolean> visited = new ConcurrentHashMap<>();
    private final ExecutorService workers = Executors.newFixedThreadPool(5);
    private final List<Future<String>> futures = new ArrayList<>();

    public List<Future<String>> crawl(String startUrl) {
        System.out.println(Thread.currentThread().getName() + " -> Started crawling - " + startUrl);
        urlQueue.offer(startUrl);
        while(!urlQueue.isEmpty()) {
            String url = urlQueue.poll();
            if (url != null && !visited.containsKey(url)) {
                visited.put(url, true);

                // Crawl this url, need to submit to workers and add the results to futures
                Future<String> future = workers.submit(() -> {
                    String result = Thread.currentThread().getName() + " -> " + url + " has been crawled.";
                    return result;
                });
                futures.add(future);

                // Get nested urls for this url
                List<String> nestedUrls = UrlConfig.urls.getOrDefault(url, Collections.emptyList());
                nestedUrls.forEach(urlQueue::offer);
            }
        }
//        workers.shutdown();
        return futures;
    }

    public void shutdown(long waitTimeInSecs) {
        workers.shutdown();
        try {
            workers.awaitTermination(waitTimeInSecs, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


}
