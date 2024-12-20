package org.example.springkeycloak.Conf;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.Collections;
import java.util.logging.Logger;


@Component
public class DebugFilter extends OncePerRequestFilter {
    private static final org.slf4j.Logger logger = LoggerFactory.getLogger(SecurityConfig.class);

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        logger.info("=== Debug Filter Start ===");
        logger.info("Request URI: {}"+ request.getRequestURI());
        logger.info("Request Method: {}"+ request.getMethod());

        // Log all headers
        logger.info("Headers:");
        Collections.list(request.getHeaderNames()).forEach(headerName ->
                logger.info("{}: {}"+ headerName+ request.getHeader(headerName))
        );

        // Check Authorization header specifically
        String authHeader = request.getHeader("Authorization");
        if (authHeader != null) {
            logger.info("Authorization header is present and starts with: {}"+
                    authHeader.substring(0, Math.min(authHeader.length(), 20)) + "...");
        } else {
            logger.info("No Authorization header found!");
        }

        // Log authentication status before filter chain
        Authentication authBefore = SecurityContextHolder.getContext().getAuthentication();
        logger.info("Authentication before filter chain: {}"+ authBefore);

        // Execute filter chain
        filterChain.doFilter(request, response);

        // Log authentication status after filter chain
        Authentication authAfter = SecurityContextHolder.getContext().getAuthentication();
        logger.info("Authentication after filter chain: {}"+ authAfter);
        if (authAfter != null) {
            logger.info("Authentication details after:");
            logger.info("IsAuthenticated: {}"+ authAfter.isAuthenticated());
            logger.info("Principal: {}"+ authAfter.getPrincipal());
            logger.info("Authorities: {}"+ authAfter.getAuthorities());
        }

        logger.info("Response Status: {}"+ response.getStatus());
        logger.info("=== Debug Filter End ===");
    }
}