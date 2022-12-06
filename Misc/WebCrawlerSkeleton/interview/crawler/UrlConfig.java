package com.example.interview.crawler;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UrlConfig {
    public static final Map<String, List<String>> urls = new HashMap<String, List<String>>() {{
        put("url1", Arrays.asList("url1.1", "url1.2", "url1.3", "url1.4", "url1.5", "url1.6", "url1.7"));
        put("url2", Arrays.asList("url2.1", "url2.2", "url2.3", "url2.4", "url2.5", "url2.6", "url2.7"));
        put("url3", Arrays.asList("url3.1", "url3.2", "url3.3", "url3.4", "url3.5", "url3.6", "url3.7"));
        put("url4", Arrays.asList("url4.1", "url4.2", "url4.3", "url4.4", "url4.5", "url4.6", "url4.7"));
        put("url5", Arrays.asList("url5.1", "url5.2", "url5.3", "url5.4", "url5.5", "url5.6", "url5.7"));
    }};


}
