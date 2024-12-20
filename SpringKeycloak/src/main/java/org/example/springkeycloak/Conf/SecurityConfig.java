package org.example.springkeycloak.Conf;

import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationConverter;
import org.springframework.security.oauth2.server.resource.authentication.JwtGrantedAuthoritiesConverter;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import java.util.Collection;



@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {
    private static final org.slf4j.Logger logger = LoggerFactory.getLogger(SecurityConfig.class);

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        logger.info("Configuring SecurityFilterChain");

        http
                .csrf(csrf -> {
                    csrf.disable();
                    logger.info("CSRF disabled");
                })
                .authorizeHttpRequests(auth -> {
                    auth.requestMatchers("/api/public/**").permitAll()
                            .anyRequest().authenticated();
                    logger.info("Configure authorize requests: /api/public/** permitted, others require auth");
                })
                .addFilterBefore(debugFilter(), UsernamePasswordAuthenticationFilter.class)
                .oauth2ResourceServer(oauth2 -> {
                    oauth2.jwt(jwt -> {
                        jwt.jwtAuthenticationConverter(jwtAuthenticationConverter())
                                .jwkSetUri("http://localhost:8180/realms/OCR-Realm/protocol/openid-connect/certs");
                        logger.info("Configured OAuth2 resource server with JWT authentication");
                    });
                })
                .sessionManagement(session -> {
                    session.sessionCreationPolicy(SessionCreationPolicy.STATELESS);
                    logger.info("Session management set to STATELESS");
                })
                .exceptionHandling(ex -> ex
                        .authenticationEntryPoint((request, response, authException) -> {
                            logger.info("Authentication failed" + authException);
                            logger.info("Authentication error message: {}"+ authException.getMessage());
                            if (authException.getCause() != null) {
                                logger.info("Caused by: {}"+ authException.getCause().getMessage());
                            }
                            response.sendError(HttpServletResponse.SC_UNAUTHORIZED,
                                    "Authentication failed: " + authException.getMessage());
                        }));

        return http.build();
    }

    @Bean
    public DebugFilter debugFilter() {
        return new DebugFilter();
    }

    @Bean
    public JwtAuthenticationConverter jwtAuthenticationConverter() {
        logger.info("Creating JwtAuthenticationConverter");

        JwtGrantedAuthoritiesConverter grantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
        grantedAuthoritiesConverter.setAuthoritiesClaimName("realm_access.roles");
        grantedAuthoritiesConverter.setAuthorityPrefix("");

        logger.info("Configured JwtGrantedAuthoritiesConverter with claim name: realm_access.roles");

        JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(jwt -> {
            Collection<GrantedAuthority> authorities = grantedAuthoritiesConverter.convert(jwt);

            logger.info("Converting JWT to authorities");
            logger.info("JWT Headers: {}"+ jwt.getHeaders());
            logger.info("JWT Claims: {}"+ jwt.getClaims());
            logger.info("JWT Subject: {}"+ jwt.getSubject());
            logger.info("JWT Issuer: {}"+ jwt.getIssuer());
            logger.info("JWT Audience: {}"+ jwt.getAudience());
            logger.info("Extracted Authorities: {}"+ authorities);

            return authorities;
        });

        return jwtAuthenticationConverter;
    }
}