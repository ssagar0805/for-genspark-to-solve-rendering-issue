import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { HashRouter, Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
// Temporarily comment out these imports to test
// import Archive from "./pages/Archive";
// import Authority from "./pages/Authority";
// import Learn from "./pages/Learn";
// import Results from "./pages/Results";
// import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <HashRouter>
        <Routes>
          <Route path="/" element={<Index />} />
          {/* Temporarily comment out other routes */}
          {/* <Route path="/archive" element={<Archive />} /> */}
          {/* <Route path="/authority" element={<Authority />} /> */}
          {/* <Route path="/learn" element={<Learn />} /> */}
          {/* <Route path="/results" element={<Results />} /> */}
          <Route path="*" element={<div>Page not found</div>} />
        </Routes>
      </HashRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
