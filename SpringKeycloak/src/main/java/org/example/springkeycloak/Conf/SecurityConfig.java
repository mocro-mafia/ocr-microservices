package org.example.springkeycloak.Conf;

import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.web.SecurityFilterChain;



@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {
    private static final org.slf4j.Logger logger = LoggerFactory.getLogger(SecurityConfig.class);

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        logger.info("Configuring SecurityFilterChain");

        http
                .csrf(AbstractHttpConfigurer::disable)
                .authorizeHttpRequests(req ->
                        req
                                .requestMatchers("/api/public/**").permitAll()
                                .requestMatchers("/api/user/**").hasRole("USER")
                                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                                .anyRequest().authenticated()
                )
                .oauth2ResourceServer(auth -> auth.jwt(token -> token.jwtAuthenticationConverter(new KeycloakJwtAuthenticationConverter())));

        return http.build();

    }
}


//    @Bean
//    public JwtAuthenticationConverter jwtAuthenticationConverter() {
//        logger.info("Creating JwtAuthenticationConverter");
//
//        JwtGrantedAuthoritiesConverter grantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
//        grantedAuthoritiesConverter.setAuthoritiesClaimName("realm_access.roles");
//        grantedAuthoritiesConverter.setAuthorityPrefix("");
//
//        logger.info("Configured JwtGrantedAuthoritiesConverter with claim name: realm_access.roles");
//
//        JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
//        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(jwt -> {
//            Collection<GrantedAuthority> authorities = grantedAuthoritiesConverter.convert(jwt);
//
//            logger.info("Converting JWT to authorities");
//            logger.info("JWT Headers: {}" + jwt.getHeaders());
//            logger.info("JWT Claims: {}" + jwt.getClaims());
//            logger.info("JWT Subject: {}" + jwt.getSubject());
//            logger.info("JWT Issuer: {}" + jwt.getIssuer());
//            logger.info("JWT Audience: {}" + jwt.getAudience());
//            logger.info("Extracted Authorities: {}" + authorities);
//
//            return authorities;
//        });
//
//        return jwtAuthenticationConverter;
//    }
