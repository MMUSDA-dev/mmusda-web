! function() {
    function l(b) {
        for (var k, a, e, d, c = [], f = 0; f < q.length; f++) {
            var g = q[f];
            if (g.Tag === b) {
                c = g.CategoryId;
                break
            }
            var h = (k = g.Tag, d = e = a = void 0, a = -1 !== (d = k).indexOf("http:") ? d.replace("http:", "") : d.replace("https:", ""), -1 !== (e = a.indexOf("?")) ? a.replace(a.substring(e), "") : a);
            if (b && (-1 !== b.indexOf(h) || -1 !== g.Tag.indexOf(b))) {
                c = g.CategoryId;
                break
            }
        }
        if (!c.length && t) {
            var u = function(a) {
                var g = document.createElement("a");
                g.href = a;
                a = g.hostname.split(".");
                return -1 !== a.indexOf("www") || 2 < a.length ? a.slice(1).join(".") :
                    g.hostname
            }(b);
            v.some(function(a) {
                return a === u
            }) && (c = ["C0004"])
        }
        return c
    }

    function h(b) {
        return b && window.OptanonActiveGroups && b.every(function(b) {
            return -1 !== window.OptanonActiveGroups.indexOf(b)
        })
    }

    function m(b) {
        return -1 !== (b.getAttribute("class") || "").indexOf("optanon-category")
    }

    function n(b) {
        return b.hasAttribute("data-ot-ignore")
    }
    var q = JSON.parse('[{"Host":"adventist.org","Tag":"https://www.googletagmanager.com/gtag/js","CategoryId":["C0002"]},{"Host":"adventist.org","Tag":"https://www.google-analytics.com/analytics.js","CategoryId":["C0002"]}]'),
        t = JSON.parse("true"),
        v = "addthis.com addtoany.com adsrvr.org amazon-adsystem.com bing.com bounceexchange.com bouncex.net criteo.com criteo.net dailymotion.com doubleclick.net everesttech.net facebook.com facebook.net googleadservices.com googlesyndication.com krxd.net liadm.com linkedin.com outbrain.com rubiconproject.com sharethis.com taboola.com twitter.com vimeo.com yahoo.com youtube.com".split(" "),
        p = ["embed", "iframe", "img", "script"];
    (new MutationObserver(function(b) {
        Array.prototype.forEach.call(b,
            function(b) {
                Array.prototype.forEach.call(b.addedNodes, function(a) {
                    var b, d;
                    if (1 === a.nodeType && -1 !== p.indexOf(a.tagName.toLowerCase()) && !m(a) && !n(a))
                        if ("script" === a.tagName.toLowerCase()) {
                            if ((d = l(b = a.src || "")).length) {
                                var c = d.join("-"),
                                    e = a.getAttribute("class") ? a.getAttribute("class") : "";
                                a.setAttribute("class", "optanon-category-" + c + " " + e);
                                h(d) || (a.type = "text/plain");
                                var f = function(b) {
                                    "text/plain" === a.getAttribute("type") && b.preventDefault();
                                    a.removeEventListener("beforescriptexecute", f)
                                };
                                a.addEventListener("beforescriptexecute",
                                    f)
                            }
                        } else(d = l(b = a.src || "")).length && (c = d.join("-"), e = a.getAttribute("class") ? a.getAttribute("class") : "", a.setAttribute("class", "optanon-category-" + c + " " + e), h(d) || (a.removeAttribute("src"), a.setAttribute("data-src", b)))
                });
                var a = b.target;
                if (b.attributeName && (!m(a) || !n(a)))
                    if ("script" === a.nodeName.toLowerCase()) {
                        if ((f = l(c = a.src || "")).length) {
                            b = f.join("-");
                            var e = a.getAttribute("class") ? a.getAttribute("class") : "";
                            a.setAttribute("class", "optanon-category-" + b + " " + e + " ");
                            h(f) || (a.type = "text/plain");
                            var d =
                                function(b) {
                                    "text/plain" === a.getAttribute("type") && b.preventDefault();
                                    a.removeEventListener("beforescriptexecute", d)
                                };
                            a.addEventListener("beforescriptexecute", d)
                        }
                    } else if (-1 !== p.indexOf(b.target.nodeName.toLowerCase())) {
                    var c, f;
                    (f = l(c = a.src || "")).length && (b = f.join("-"), e = a.getAttribute("class") ? a.getAttribute("class") : "", a.setAttribute("class", "optanon-category-" + b + " " + e), h(f) || (a.removeAttribute("src"), a.setAttribute("data-src", c)))
                }
            })
    })).observe(document.documentElement, {
        childList: !0,
        subtree: !0,
        attributes: !0,
        attributeFilter: ["src"]
    });
    var r = document.createElement;
    document.createElement = function() {
        for (var b = [], k = 0; k < arguments.length; k++) b[k] = arguments[k];
        if ("script" !== b[0].toLowerCase() && -1 === p.indexOf(b[0].toLowerCase())) return r.bind(document).apply(void 0, b);
        var a = r.bind(document).apply(void 0, b),
            e = a.setAttribute.bind(a);
        return Object.defineProperties(a, {
            src: {
                get: function() {
                    return a.getAttribute("src") || ""
                },
                set: function(d) {
                    var c = "";
                    "string" == typeof d ? c = d : d instanceof Object && (c = d.toString());
                    c = l(c);
                    return !c.length || "script" !== b[0].toLowerCase() || m(a) || h(c) || n(a) ? !c.length || -1 === p.indexOf(b[0].toLowerCase()) || m(a) || h(c) || n(a) ? e("src", d) : (a.removeAttribute("src"), e("data-src", d)) : (e("type", "text/plain"), e("src", d)), !0
                }
            },
            type: {
                set: function(b) {
                    var c = l(a.src || "");
                    b = !c.length || m(a) || h(c) || n(a) ? b : "text/plain";
                    return e("type", b), !0
                }
            }
        }), a.setAttribute = function(b, c, f) {
            "type" !== b && "src" !== b || f ? e(b, c) : a[b] = c
        }, a
    }
}();