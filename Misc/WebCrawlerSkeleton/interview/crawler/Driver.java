package com.example.interview.crawler;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

@Component
public class Driver {
    public void start(ApplicationContext applicationContext) {
        ExecutorService crawlWorkers = Executors.newFixedThreadPool(3);

        List<String> urls = Arrays.asList("url1", "url2", "url3", "url4", "url5");
        urls.forEach(url -> {
            WebCrawler webCrawler = applicationContext.getBean(WebCrawler.class);
            System.out.println(webCrawler);
            crawlWorkers.execute(() -> {
                for (Future<String> future : webCrawler.crawl(url)) {
                    if (future.isDone()) {
                        try {
                            System.out.println(Thread.currentThread().getName() + " -> " + "Result - " + future.get());
                        } catch (InterruptedException | ExecutionException e) {
                            e.printStackTrace();
                        }
                    }
                }
                webCrawler.shutdown(120);
            });
        });

        crawlWorkers.shutdown();
    }
}

