import { useState } from "react";
import { motion } from "framer-motion";

// ✅ Custom replacements for missing ShadCN components

const Button = ({ children, ...props }) => (
  <button
    {...props}
    className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition disabled:opacity-50"
  >
    {children}
  </button>
);

const Card = ({ children }) => (
  <div className="border rounded-lg shadow-sm bg-white">{children}</div>
);

const CardContent = ({ children, className = "" }) => (
  <div className={`p-4 ${className}`}>{children}</div>
);

const Input = (props) => (
  <input
    {...props}
    className="border p-2 w-full rounded text-sm"
  />
);

const Textarea = (props) => (
  <textarea
    {...props}
    className="border p-2 w-full rounded text-sm"
  />
);

export default function WorkflowBuilder() {
  const [prompt, setPrompt] = useState("");
  const [model, setModel] = useState("gpt-4");
  const [output, setOutput] = useState("");
  const [running, setRunning] = useState(false);

  const runWorkflow = async () => {
    setRunning(true);
    try {
      const response = await fetch("http://localhost:8000/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_input: prompt,
          model_name: model,
          temperature: 0.7,
        }),
      });
      const data = await response.json();
      setOutput(data.output);
    } catch (err) {
      setOutput("Error running workflow.");
    } finally {
      setRunning(false);
    }
  };

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-2 gap-4">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="space-y-4"
      >
        <Card>
          <CardContent className="space-y-2">
            <label className="font-semibold">System Prompt</label>
            <Textarea
              rows={2}
              placeholder="You are a helpful assistant."
              disabled
            />
            <label className="font-semibold">User Input</label>
            <Textarea
              rows={3}
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Ask something..."
            />
            <label className="font-semibold">Model</label>
            <Input
              value={model}
              onChange={(e) => setModel(e.target.value)}
              placeholder="gpt-4, mistral, etc."
            />
            <Button onClick={runWorkflow} disabled={running}>
              {running ? "Running..." : "Run Workflow"}
            </Button>
          </CardContent>
        </Card>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="space-y-4"
      >
        <Card>
          <CardContent>
            <label className="font-semibold block mb-2">Output</label>
            <Textarea rows={8} value={output} readOnly />
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}
