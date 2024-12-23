package org.example.springkeycloak.Controller;

import org.example.springkeycloak.DTO.RegisterDTO;
import org.example.springkeycloak.Service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.jwt.Jwt;
import org.springframework.web.bind.annotation.*;
import java.util.Map;
import java.util.logging.Logger;


@RestController
@RequestMapping("/api")
public class AuthController {
    @Autowired
    private AuthService authService;

    private static final Logger logger = Logger.getLogger(AuthController.class.getName());
    @GetMapping("/public/test")
    public String test() {
        return "Public endpoint works!";
    }

    @PostMapping("/public/register")
    public Map<String,Object> register(@RequestBody RegisterDTO registerDTO) {
        Map<String,Object> response = authService.registerUser(registerDTO);
        logger.info("response status : " + response.get("status"));
        logger.info("response body : " + response.get("body"));
        return response;
    }


    @GetMapping("/user")
    @PreAuthorize("hasAuthority('User') or hasAuthority('USER')")
    public String userEndpoint(@AuthenticationPrincipal Jwt jwt) {
        System.out.println(jwt.getClaims());
        return "Hello, " + jwt.getClaimAsString("preferred_username");
    }

    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public String adminEndpoint() {
        return "Hello, Admin!";
    }

}