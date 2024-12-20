package org.example.springkeycloak.Controller;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.oauth2.jwt.Jwt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;


@RestController
@RequestMapping("/api")
public class AuthController {
    @GetMapping("/public/test")
    public String test() {
        return "Public endpoint works!";
    }


    @GetMapping("/user")
    @PreAuthorize("hasAuthority('User') or hasAuthority('USER')")
    public String userEndpoint(@AuthenticationPrincipal Jwt jwt) {
        System.out.println(jwt.getClaims());
        return "Hello, " + jwt.getClaimAsString("preferred_username");
    }
    @GetMapping("/api/user2")
    public String userEndpoint2(@AuthenticationPrincipal Jwt jwt) {
        System.out.println("I am here \n\n\n\n\n");
        // Debugging roles
        var authorities = SecurityContextHolder.getContext().getAuthentication().getAuthorities();
        System.out.println("Authorities: ");
        for (GrantedAuthority authority : authorities) {
            System.out.println(authority.getAuthority());
        }

        return "Hello, " + jwt.getClaimAsString("preferred_username");
    }

    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public String adminEndpoint() {
        return "Hello, Admin!";
    }
    @GetMapping("/api/test-auth")
    public ResponseEntity<?> testAuth(@AuthenticationPrincipal Jwt jwt) {
        Map<String, Object> response = new HashMap<>();
        response.put("token_claims", jwt.getClaims());
        response.put("authorities", SecurityContextHolder.getContext()
                .getAuthentication().getAuthorities());
        return ResponseEntity.ok(response);
    }
}